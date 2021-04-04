from django.urls import path
import resume_builder.views as rb_views
urlpatterns = [
    path('contact/', rb_views.contact,name="resume-contact"),
    path('about/',rb_views.about,name="resume-about"),
    path('skills/',rb_views.skills,name="resume-skills"),
    path('skills/edit/<int:id>',rb_views.skills_edit,name="resume-skills-edit"),
    path('skills/delete/<int:id>',rb_views.skills_delete,name="resume-skills-delete"),
    path('education/',rb_views.education,name="resume-education"),
    path('education/edit/<int:id>',rb_views.education_edit,name="resume-education-edit"),
    path('educaiton/delete/<int:id>',rb_views.education_delete,name="resume-education-delete"),
    path('IExperience/',rb_views.internship,name="resume-internship"),
    path('IExperience/edit/<int:id>',rb_views.internship_edit,name="resume-internship-edit"),
    path('IExperience/delete/<int:id>',rb_views.internship_delete,name="resume-internship-delete"),
    path('training/',rb_views.training,name="resume-training"),
    path('training/edit/<int:id>',rb_views.training_edit,name="resume-training-edit"),
    path('training/delete/<int:id>',rb_views.training_delete,name="resume-training-delete"),
    path('project/',rb_views.project,name="resume-project"),
    path('project/edit/<int:id>',rb_views.project_edit,name="resume-project-edit"),
    path('project/delete/<int:id>',rb_views.project_delete,name="resume-project-delete"),
    path('extra/',rb_views.extra,name="resume-extra"),
    path('extra/edit/<int:id>', rb_views.extra_edit, name="resume-extra-edit"),
    path('extra/delete/<int:id>', rb_views.extra_delete, name="resume-extra-delete"),
    path('language/',rb_views.language,name="resume-language"),
    path('language/edit/<int:id>',rb_views.language_edit,name="resume-language-edit"),
    path('language/delete/<int:id>',rb_views.language_delete,name="resume-language-delete"),
    path('pi/edit/<int:id>',rb_views.pi_edit,name="resume-pi-edit"),
    path('pi/delete/<int:id>',rb_views.pi_delete,name="resume-pi-delete"),
    path('pi/',rb_views.pi,name="resume-pi"),
    path('achievement/',rb_views.achievement,name="resume-achievement"),
    path('achievement/edit/<int:id>',rb_views.achievement_edit,name="resume-achievement-edit"),
    path('achievement/delete/<int:id>',rb_views.achievement_delete,name="resume-achievement-delete"),
    path('declaration/',rb_views.declaration,name="resume-declaration"),
    path('other/',rb_views.other,name="resume-other"),
    path('other/edit/<int:id>',rb_views.other_edit,name="resume-other-edit"),
    path('other/delete/<int:id>',rb_views.other_delete,name="resume-other-delete"),
    #path('verify/',rb_views.verify,name="verify")
    #path('generate/',rb_views.generate,name="generate")
]
