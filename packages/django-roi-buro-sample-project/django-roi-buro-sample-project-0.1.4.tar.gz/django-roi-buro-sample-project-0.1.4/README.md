# ROI BURO sample project

## Name
ROI BURO sample test project

## Description
This is Django-based sample test project which collect information about CPU usage and shows this stats at HTML page.
There are client - linux daemon written on Python, which measures CPU utilization periodically and server - django application, which receives measures via REST API.

## Installation

1. Add "roiburo" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
        ...
        'roiburo',
    ]

2. Include the sample project URLconf in your project urls.py like this:

    path('roi-buro/', include('roiburo.urls')),

3. Run ``python manage.py migrate`` to create project models.

4. Start the development server and send POST request to http://127.0.0.1:8000/api/v1/core/system-states
   to create a cpu usage record.

5. Start daemon from ``client`` folder by running ``python main.py``.

6. Visit http://127.0.0.1:8000/api/v1/core/system-state-details to view statistics.

7. API docs is available at http://127.0.0.1:8000/api/schema/swagger-ui#/

## Project status
Completed

## Features

-   Django 3.2
-   Python 3.9
-   [12-Factor](http://12factor.net/) based settings via [django-environ](https://github.com/joke2k/django-environ)
-   Optimized settings
-   OpenAPI based docs via [drf-spectacular](https://github.com/tfranzel/drf-spectacular)