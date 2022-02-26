from django.urls import path
from Proctor import views

urlpatterns = [
    path("",views.Login1,name='Login1'),
    path("Login2",views.Login2,name='Login2'),
    path("Login3",views.Login3,name='Login3'),
    path("Login4",views.Login4,name='Login4'),
    path("signup",views.SignUp, name="SignUp"),
    path("signupSuccess",views.SignupSuccess, name="SignupSuccess"),
    path("details",views.SignupDetails, name="SignupDetails"),
    path("sLogout",views.sLogout, name="sLogout"),
    path("pLogout",views.pLogout, name="pLogout"),
    path("student",views.StudentLogin, name="StudentLogin"),
    path("proctor",views.ProctorLogin, name="ProctorLogin"),
    path("coordinator",views.CoordinatorLogin, name="CoordinatorLogin"),
    path("sDashboard",views.sDashboard, name="sDashboard"),
    path("sActivities",views.sActivities, name="sActivities"),
    path("Newactivity",views.Newactivity, name="Newactivity"),
    path("sRecords",views.sRecords, name="sRecords"),
    path("updateSDb",views.updateSDb, name="updateSDb"),
    path("updatePDb",views.updatePDb, name="updatePDb"),
    path("updateSuppDb",views.updateSuppDb, name="updateSuppDb"),
    path("updateCDb",views.updateCDb, name="updateCDb"),
    path("updateRDb",views.updateRDb, name="updateRDb"),
    path("updatePP",views.updatePP, name="updatePP"),
    path("pDashboard",views.pDashboard, name="pDashboard"),
    path("Announce",views.Announce, name="Announce"),
    path("Manage",views.Manage, name="Manage"),
    path("kickstudent",views.Kickstudent, name="Kickstudent"),
    path("pStudentlist",views.pStudentlist, name="pStudentlist"),
    path("ViewStudent",views.ViewStudent, name="ViewStudent"),
    path("ViewActivity",views.ViewActivity, name="ViewActivity"),
    path("Recordupdateform/<str:stu>/<int:id>",views.Recordupdateform, name="Recordupdateform"),
    path("Recordupdateform/<str:stu>/<str:stun>",views.SignupDetails, name="SignupDetails"),
    path("ForgotPassword",views.forgotPass, name="ForgotPassword"),
    path("Supplementary",views.supplementary, name="Supplementary"),
    path("RejectAct",views.rejectAct, name="RejectAct"),
    path("Help",views.Help, name="Help"),
    path("About",views.About, name="About"),
    path("Report",views.Report, name="Report"),
    path("Tutorial",views.Tutorial, name="Tutorial"),
    path("Reportform",views.Reportform, name="Reportform"),
    path("UploadRes",views.UploadRes, name="UploadRes"),
]
