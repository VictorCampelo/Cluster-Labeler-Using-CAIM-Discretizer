from caibal import Caibal

c = Caibal()

print(c.execute(path='Datasets/ffiresData.csv', 
      cluster_alg=1, 
      discretization_type=1, 
      var=10.5, 
      n_clusters=3, 
      prepro=False, 
      is_sklearn_df=True, 
      sklearn_df_name="iris",
      has_index_column=False,
      index_column_name="1",
      has_target=False, 
      has_column_name=False,
      verbose=False)
      )
