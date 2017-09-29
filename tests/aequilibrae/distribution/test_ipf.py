from unittest import TestCase
import numpy as np
import os, tempfile

from aequilibrae.distribution import Ipf
from aequilibrae.matrix import AequilibraEData, AequilibraeMatrix
from tests.clean_after_tests import clean_after_tests

zones = 100

# row vector
args = {'entries': zones,
        'field_names': ['rows'],
        'data_types': [np.float64],
        'memory_mode': True}
row_vector = AequilibraEData(**args)
row_vector.rows[:] = np.random.rand(zones)[:] * 1000
row_vector.index[:] = np.arange(zones)[:]
# column vector
args['field_names'] = ['columns']
column_vector = AequilibraEData(**args)
column_vector.columns[:] = np.random.rand(zones)[:] * 1000
column_vector.index[:] = np.arange(zones)[:]
# balance vectors
column_vector.columns[:] = column_vector.columns[:] * (row_vector.rows.sum()/column_vector.columns.sum())

# seed matrix_procedures
name_test = AequilibraeMatrix().random_name()
args = {'file_name': name_test,
        'zones': zones,
        'matrix_names': ['seed']}

matrix = AequilibraeMatrix()
matrix.create_empty(**args)
matrix.seed[:, :] = np.random.rand(zones, zones)[:,:]
matrix.computational_view(['seed'])
matrix.index[:] = np.arange(zones)[:]


class TestIpf(TestCase):
    def test_fit(self):
        # The IPF per se
        args = {'matrix': matrix,
                'rows': row_vector,
                'row_field': 'rows',
                'columns': column_vector,
                'column_field': 'columns'}

        fratar = Ipf(**args)
        fratar.fit()

        result = fratar.output

        if result.seed.sum() != result.seed.sum():
            self.fail('Ipf did not converge')

        if fratar.gap > fratar.parameters['convergence level']:
            self.fail('Ipf did not converge')



