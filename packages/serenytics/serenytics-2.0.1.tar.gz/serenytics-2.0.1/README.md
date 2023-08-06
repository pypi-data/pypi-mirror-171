# Serenytics Python Client

[Serenytics](https://www.serenytics.com) is a hosted or on-premises platform to analyze, visualize and share your data.
With Serenytics you can create custom dashboards that fit your exact needs.

The Serenytics Python Client main features are:

- create a new data source
- reload data in a source
- push new data in a source
- extract data from a source using our full data processing API

You can use all these features inside your custom python scripts that you can run and schedule on
 [Serenytics](https://www.serenytics.com).

[Full Serenytics developer documentation](http://serenytics.readme.io)


## Setup

To setup your project, follow these steps:

 1. Install Serenytics using pip: `pip install --upgrade serenytics`.
 1. Initialize the client with your API key. You can find your key on 
 [your Serenytics account](https://app.serenytics.com/studio/account).
 
 Note: when running the script on Serenytics platform, the `api_key`
 param is not required, it is set automatically.

```python
import serenytics

client = serenytics.Client(api_key='YOUR_API_KEY')
```

## Quickstart

Example script:

```python
import serenytics

client = serenytics.Client(api_key='YOUR_API_KEY')

data_source = client.get_or_create_storage_data_source_by_name('new_data_source')

data_source.reload_data([
    {'year': 2015, 'quarter': 'Q1', 'sales': 120},
    {'year': 2015, 'quarter': 'Q2', 'sales': 80},
    {'year': 2015, 'quarter': 'Q4', 'sales': 25},
    {'year': 2014, 'quarter': 'Q2', 'sales': 85},
])
```  

## Run your script on your machine

When writing your script, you often want to use your favorite IDE or text editor on your machine. You can use a
virtualenv and install all the dependencies with:
    
    pip install -r requirements.txt
    
or run the script with docker:

    docker run --rm -it -v $(pwd):/usr/src/app serenytics/serenytics-python-client:RELEASE python YOUR_SCRIPT.py
    
where you have to replace `YOUR_SCRIPT.py` with the name of your python file and `RELEASE` with the last release of
the serenytics python client (e.g.: 0.2).
