imp urls:
   path('',home,name="home"),
   path('create/',create,name="create"),
   path('edit/<int:pk>/',edit,name="edit"),
   path('delete/<int:pk>/',delete,name="delete"),
   path('deleteall/',deleteall,name="deleteall")
