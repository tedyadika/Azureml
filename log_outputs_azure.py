# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 18:59:16 2022

@author: aokelo
"""

from azureml.core import Workspace,Datastore,Dataset,Experiment


## create or get workspace 
ws = Workspace.get(name='rffffefefaffht4ht',
                    subscription_id='fffnfnfnfn02-gfffrrrr',
                    resource_group='DSCGlobalCEEDTANLTst',
                    #create_resource_group=False,
                    #location='WestEurope'
                    )

our_store =Datastore.get(ws, 'azure_sdk_blob')



### Create experiment 
experiment = Experiment(workspace = ws,
                        name = 'picks_experiment')

### run an experiment
new_run = experiment.start_logging()

#### do your staff here
##########################################################################################

### get the datasets 
ml_dataset = Dataset.get_by_name(ws, 'picks_dataset_sdk')
df = ml_dataset.to_pandas_dataframe()

nulldf = df.isnull().sum()

for col in df.columns:
    new_run.log(col, nulldf[col])



###### complete the experiment

new_run.complete()
