from azureml.core import Workspace,Datastore,Dataset


## create or get workspace 
ws = Workspace.get(name='put_workspace name',
                    subscription_id='add id here',
                    resource_group='add resource group name',
                    #create_resource_group=False,
                    #location='WestEurope'
                    )

### create Datastore

our_store = Datastore.register_azure_blob_container(
                                                    workspace = ws,
                                                    datastore_name ='how do yo wanna name your store',
                                                    account_name ='account name',
                                                    container_name = "from which container is the data",
                                                    account_key ='add key')

### create and register dataset
our_store =Datastore.get(ws, 'azure_sdk_blob')

data_path = [(our_store,'silver/czche_2/OUT_ORDERS_PICKS/*')]

## create dataset
picks_dataset = Dataset.Tabular.from_parquet_files(path=data_path)

### Register the dataset
picks_dataset = picks_dataset.register(workspace = ws,
                                       name = 'picks_dataset_sdk',
                                       create_new_version = True)

### get the datasets 
ml_dataset = Dataset.get_by_name(ws, 'picks_dataset_sdk')
df = ml_dataset.to_pandas_dataframe()

### modify data

df_edit =df[['DATE','Year','Month']]



### save data output back to azure ml dataset

az_ds_dt = Dataset.Tabular.register_pandas_dataframe(dataframe =df_edit,
                                                  target = our_store,
                                                  name = 'edited_data')
