def run_distribution_models(qgis_project):
    from qaequilibrae.modules.distribution_procedures import DistributionModelsDialog
    if qgis_project.project is None:
        qgis_project.iface.messageBar().pushMessage("Error", "You need to load a project first", level=3, duration=10)
        return
    dlg2 = DistributionModelsDialog(qgis_project)
    dlg2.show()
    dlg2.exec_()
