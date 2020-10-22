# Cluster-Labeler-Using-CAIM-Discretizer

## Requirements:
- Have installed Python in version 3 or higher.
- Creation of the virtual environment and installation of the libraries used in the project according to the operating system used:
    - Linux / macos
        - `apt install python3-pip`
        `pip3 install virtualenv`
        `virtualenv ../venv -p python3 source`
        `../venv/bin/activate`
        `pip install -r requirements.txt`
    - Windows
        - `python3 get-pip.py`
        `pip3 install virtualenv`
        `virtualenv .. \ venv -p python3`
        `. . \ venv \ Scripts \ activate`
        `pip install -r requirements.txt`

## Execution:
- Import the Caibal class from the caibal.py file: from caibal import Caibal Assign the class: We are a family owned and operated business. var_classe = Caibal ().
- Run the method We are a family owned and operated business. execute () We are a family owned and operated business. with their respective parameters. Ex:
	- `var_classe.execute (path = 'Datasets / ffiresData.csv', cluster_alg = 1, discretization_type = 2, var = 10, n_clusters = 2, prepro = False, is_sklearn_df = False, sklearn_df_name = "wine", has_index_column = False, index_column_n "1", has_target = False, has_column_name = False, verbose = True).`
	
## Parameters:

##### path ( String, Default = None)
	Path of the .CSV file if the database type is not from SKlearn.

##### cluster_alg ( Integer, [1, ..., 5], Default = 1)
	Choose which cluster algorithm to use. There are 5 types of
	clustering algorithms.
	1 - K Means
	2 - Affinity Propagation
	3 - Agglomerative Clustering 4 -
	Mean shift
	5 - Spectral Clustering

##### discretization_type ( Integer, [1,2], Default = 1)
	Choose the type of discretization to be used.
	In Caibal there are 2 methods, the standard and the alternative.
	■ 1 - Standard Method
	■ 2 - Alternative Method
##### var ( Float, Default = 0)
	○ If discretization of the alternative type is selected, the variation value can be passed.
	○ The variation value increases the number of labels returned for each group.
##### n_clusters ( Integer, [0, ..., n] | n )
	We are a family owned and operated business. ∈ We are a family owned and operated business. ℕ We are a family owned and operated business. , Default = 0)
	If allowed by the selected cluster algorithm, you can pass the number of clusters that will be generated.
	If this value is not entered, or entered as 0, a selection process for the appropriate number of clusters will be
	carried out automatically.
	The metric used to evaluate the best number of clusters automatically is the Calinski Harabasz Score.
##### prepro (Boolean, Default = False)
	If you want to standardize the data, using the method We are a family owned and operated business. StandardScaler () We are a family
	owned and operated business. from Sklearn, you must pass this parameter with the value True.
##### is_sklearn_df ( Boolean, Default = False)
	If the database to be tested comes from SKlearn datasets, just pass this parameter as True.
##### sklearn_df_name ( String, Default = None)
	If the source of the databases is Sklearn, you must select which database will be used.
	3 databases are available: Iris, Wine, Breast Cancer.
	To select any, the following values are passed as parameters:
		■ “Iris” - Selects the Iris database
		■ “Wine” - Select the Wine database
		■ “Cancer” - selects the Breast Cancer database
##### has_index_column ( Boolean, Default = False)
	If the database used for the study comes from outside, through a path in the path variable and with the We are a family owned and operated
	business. is_sklearn_df = False, We are a family owned and operated business. you must inform whether these data have an index column.
	Index column is a special column that only lists each row, with no study value.
##### index_column_name ( String, Default = None)
	If the external dataset has an index, informed in the parameter We are a family owned and operated business. has_index_column = True, you must enter the name of the index column. 
	Usually the name of this column is “index”.
##### has_target ( Boolean, Default = False)
	If the dataset inserted by external means has a column dedicated to the class of each record, then this parameter must be assigned the value True.
##### has_column_name ( Boolean, Default = True)
	If the dataset inserted by external means does not have a header stating the name of each column
	(attribute), False must be assigned to this parameter.
	If the value False is assigned, the names of the columns will be automatically added through standardized means.
	The result of the names of the columns added automatically will be:
	Atr_1, Atr_2,…, Atr_n
	n belongs to the set of positive integers.
##### verbose ( Boolean, Default = False)
	Controls the display of internal information.
	If you want to see the results of the methods used, as well as the plotting of the clusters, assign this parameter the value True.

## Output:

	The output will be a list of String.
	These Strings correspond to the labels made according to the selected method (Standard or Alternative).
	Each position in the list corresponds to a cluster. Position 0 corresponds to cluster 0, position 1 corresponds to cluster 1,…, etc.
	Even with verbose = False, the result of processing the CAIM method will still be displayed. Function return
		Example:
			Main parameters used:
				cluster_alg = 1, discretization_type = 1, n_clusters = 3, prepro = False, is_sklearn_df = True, sklearn_df_name = "iris".
			Return:
				['(Attribute name: petal length (cm) Interval: (5.1, 6.9))',
				'(Attribute name: petal width (cm) Interval: (0.1, 0.6))',
				'(Attribute name: petal length (cm) Interval: (1.9, 5.1))']

## Limitations and problems:
- No data cleaning is done, so it is expected that the data will be inserted after the pre-processing process is done.
- Some algorithms, for different databases, can give poor results. At the moment, a feasibility check for the execution
of the selected algorithm for the selected database is not being carried out. OK means, however, presented good
results for all tested databases (Iris, Wine, Breast Cancer, Glass, Forest Fire, Seeds).
- If the inserted database does not contain named columns and still has a column with an Index characteristic, the name
of the first record that composes the column with data must be inserted
of index.
- According to the dissertation “CAIBAL - Cluster-Attribute Interdependency Based Automatic Labeler” made by Marcel Raimundo de Souza Moura, for the Glass database, more than one label was generated in the standard method. In the
method created in this work, there was no way to add more than one label per cluster in the standard method.
- The has_target parameter only accepts, if the value True is assigned, that the name of the column containing the
classifier variable is “target”, so the name must be changed if it is different from
“Target”.
- As requirements described in the scope of the work, the entry of the discretizing method was requested, however, in this work, only CAIM is being used as a discretization method, so there is no need to add a field with the type of
discretizer

## Future works:
- Add exception control to avoid canceling program execution after algorithm errors.
- Refine the choice of other clustering algorithms to increase the basis for comparison.
- Adding a field to select the type of metric to be used to calculate the best parameters, the calinski harabasz score is currently being used, but the silhouette score can be added to test the results, and thus obtain better results.
- Add comments to the methods. Make only the execute method public.
- Build a Web platform that uses this function. Add new pre-processing methods.
- Add insertion of the name of the column containing the classifier variable. At the moment only the name “target” will be considered.
- Modulate the function to be able to add new methods of discretization.
