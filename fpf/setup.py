setup(
    ...
    options={
        'app': {
            'formal_name': 'My First App',
            'bundle': 'org.example',
        },
        'macos': {
            'app_requires': [
                'toga-cocoa'
            ],
            'icon': 'icons/macos',
        },
        'ios': {
            'app_requires': [
                'toga-ios'
            ],
            'icon': 'images/ios_icon',
            'splash': 'images/ios_splash',
        },
        'android': {
            'app_requires': [
                'toga-android'
            ],
            'icon': 'images/android_icon',
            'splash': 'images/android_splash',
        },
        'tvos': {
            'app_requires': [
                'toga-ios'
            ]
        },
        'django': {
            'app_requires': [
                'toga-django'
            ]
        },
    }
)