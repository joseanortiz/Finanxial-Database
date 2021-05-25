from django.urls import path
from . import views


urlpatterns = [
    #path('', views.login, name='login'),
    path('search/', views.search, name='search'),
    path('search/client-name/', views.searchCN, name='searchCN'),
    path('search-id/client-name-id/<group_id>/', views.searchCN_id, name='searchCN_id'),
    path('search/client-name/search-results/', views.searchCN_q, name='searchCN_q'),
    path('search-id/client-name-id/<group_id>/search-results-id/', views.searchCN_q_id, name='searchCN_q_id'),
    path('search/tax-ID/', views.searchTI, name='searchTI'),
    path('search-id/tax-ID-id/<group_id>/', views.searchTI_id, name='searchTI_id'),
    path('search/tax-ID/search-results/', views.searchTI_q, name='searchTI_q'),
    path('search-id/tax-ID-id/<group_id>/search-results-id/', views.searchTI_q_id, name='searchTI_q_id'),
    path('search/pm/', views.searchPM, name='searchPM'),
    path('search-id/pm-id/<group_id>/', views.searchPM_id, name='searchPM_id'),
    path('search/project-manager/search-results', views.searchPM_q, name='searchPM_q'),
    path('search-id/project-manager-id/<group_id>/search-results-id', views.searchPM_q_id, name='searchPM_q_id'),
    path('add-client/', views.client, name='client'),
    path('edit-client/<list_id>', views.edit, name='edit'),
    path('edit-client/<list_id>/view-document/', views.document_id, name='document_id'),
    path('edit-client/<list_id>/view-document/add/', views.document_id_add, name='document_id_add'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('records/', views.records, name='records'),
    path('documents/', views.document_list, name='document_list'),
    path('add-document/', views.document, name='document'),
    path('groups/', views.groups, name='groups'),
    path('group-search/<group_id>/', views.group_search, name='group_search'),
    path('groups/add-group/', views.group, name='group'),
    path('group-delete/<group_id>/', views.group_delete, name='group_delete'),
    path('edit-client/<list_id>/view-document/<file_id>/', views.edit_document, name='edit_document'),
    path('edit-client/<list_id>/view-document/<file_id>/delete/', views.delete_file, name='delete_file'),

]
