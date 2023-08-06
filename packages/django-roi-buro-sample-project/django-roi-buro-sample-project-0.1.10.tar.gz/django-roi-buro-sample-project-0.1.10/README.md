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

    path('roiburo/', include('roiburo.urls')),

3. Run ``python manage.py makemigrations roiburo`` to create project migrations.

4. Run ``python manage.py migrate`` to create models.

5. Start the development server ``python manage.py runserver``.

6. Edit daemon api_url setting in client/config.ini, set it to ``http://127.0.0.1:8000/roiburo/api/v1/core/system-states``.

7. Start daemon from ``client`` folder by running ``python main.py``.

8. Visit http://127.0.0.1:8000/roiburo/api/v1/core/system-state-details to view statistics.

9. API docs is available at http://127.0.0.1:8000/roiburo/api/schema/swagger-ui#/

## Features

-   Django 3.2
-   Python 3.9
-   [12-Factor](http://12factor.net/) based settings via [django-environ](https://github.com/joke2k/django-environ)
-   Optimized settings
-   OpenAPI based docs via [drf-spectacular](https://github.com/tfranzel/drf-spectacular)