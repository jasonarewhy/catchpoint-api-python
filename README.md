# Catchpoint API Python Module

## Description
Catchpoint has two types of APIs, a push (subscriber) API and a pull REST API. This module is a wrapper for the REST API (which is still in alpha as of June 2014).

[API documentation](https://io.catchpoint.com/ui/Help) is available to Catchpoint customers.

## Requirements

* datetime
* pytz
* requests

## Installation

`python setup.py install`

## Usage

```python
# import the module
import catchpoint

# define your catchpoint credentials
creds = {
    'client_id': 'yourclientid',
    'client_secret': 'yourclientsecret'
}

# create a Catchpoint object
cp = catchpoint.Catchpoint()

# query the API, always pass the creds
print cp.favorite_charts(creds)
print cp.favorite_details(creds, myfav)
```

### Methods

| Method  |  Description  | Parameters |
| :------ | :------------ | :--------- |
| raw     | Retrieve the raw performance chart data for a given test for a time period. | creds, testid, startTime, endTime, tz="UTC" |
| favorite_charts | Retrieve the list of favorite charts. | creds |
| favorite_details | Retrieve the favorite chart details. | creds, favid |
| favorite_data | Retrieve the data for a favorite chart, optionally overriding its timeframe or test set. | creds, favid, startTime=None, endTime=None, tz="UTC", tests=None |
| nodes | Retrieve the list of nodes for the API consumer. | creds |
| node | Retrieve a given node for the API consumer. | creds, node |

### Parameters

| Param | Type | Description |
| :---- | :--- | :---------- |
| creds | dict | Contains the Catchpoint `client_id` and `client_secret` |
| testid | str | The Catchpoint test ID |
| favid | str | The Catchpoint favorite ID |
| startTime | str or int | UTC formatted ("2014-06-19T12:51:37Z") time to begin requested dataset. Can be expressed as a negative integer when `endTime` = 'now'. |
| endTime | str | UTC formatted ("2014-06-19T12:51:37Z") time to end requested dataset. Can be expressed as 'now' to use current time. |
| tz | str | Optionally set the timezone to correlate to the Catchpoint test's configuration. |
| tests | str | Specify a comma-separated list of tests when retreiving a favorite chart.
| node | str | The Catchpoint node id. |

#### Relative Time Requests
Catchpoint's API requires specific UTC formatted timestamps when requesting datasets. These can be made relative by setting `startTime` to a negative integer that represents number of minutes into the past, and set `endTime` to 'now'.

Example:

```python
cp = catchpoint.Catchpoint()
myfav = "12345"
startTime = -5
endTime = "now"
print cp.favorite_data(creds, myfav, startTime, endTime)
```
## License

GPL v2