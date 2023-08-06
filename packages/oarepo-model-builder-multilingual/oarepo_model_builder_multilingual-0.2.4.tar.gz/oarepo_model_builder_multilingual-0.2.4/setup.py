# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oarepo_model_builder_multilingual',
 'oarepo_model_builder_multilingual.builtin_models',
 'oarepo_model_builder_multilingual.invenio',
 'oarepo_model_builder_multilingual.model_preprocessors',
 'oarepo_model_builder_multilingual.property_preprocessors']

package_data = \
{'': ['*'], 'oarepo_model_builder_multilingual.invenio': ['templates/*']}

install_requires = \
['langcodes>=3.3.0', 'oarepo-model-builder>=0.9.24']

entry_points = \
{'oarepo.model_schemas': ['es-strings = '
                          'oarepo_model_builder_multilingual:multilingual_jsonschema.json5',
                          'i18n = oarepo_model_builder_multilingual:i18n.json5',
                          'mult-settings = '
                          'oarepo_model_builder_multilingual:multilingual_settings.json5',
                          'ui = '
                          'oarepo_model_builder_multilingual:ui_jsonschema.json5'],
 'oarepo.models': ['i18n = '
                   'oarepo_model_builder_multilingual.builtin_models:i18n.json'],
 'oarepo_model_builder.builders': ['0301-invenio_record_search_options_multilang '
                                   '= '
                                   'oarepo_model_builder_multilingual.invenio.invenio_search_multilingual:InvenioRecordSearchOptionsBuilderMultilingual',
                                   '0901-invenio_multiligual_poetry = '
                                   'oarepo_model_builder_multilingual.invenio.invenio_multilingual_poetry:InvenioMultilingualPoetryBuilder',
                                   '360-invenio_schema_i18n = '
                                   'oarepo_model_builder_multilingual.invenio.invenio_schema_i18n:InvenioSchemaI18nStrBuilder',
                                   '360-invenio_schema_multilingual = '
                                   'oarepo_model_builder_multilingual.invenio.invenio_schema_multilingual:InvenioSchemaMultilingualBuilder',
                                   '380-invenio_record_dumper = '
                                   'oarepo_model_builder_multilingual.invenio.invenio_record_dumper_multilingual:InvenioRecordMultilingualDumperBuilder'],
 'oarepo_model_builder.model_preprocessors': ['30-multilingual = '
                                              'oarepo_model_builder_multilingual.model_preprocessors.multilingual:MultilingualModelPreprocessor'],
 'oarepo_model_builder.property_preprocessors': ['1001-i18n = '
                                                 'oarepo_model_builder_multilingual.property_preprocessors.i18nStr:I18nStrPreprocessor',
                                                 '700-multilingual = '
                                                 'oarepo_model_builder_multilingual.property_preprocessors.multilingual:MultilangPreprocessor',
                                                 '701-marshmallow-class-i18n = '
                                                 'oarepo_model_builder_multilingual.property_preprocessors.i18n_marshmallow_class_generator:MarshmallowClassGeneratorPreprocessor'],
 'oarepo_model_builder.sample_data_providers': ['multilingual = '
                                                'oarepo_model_builder_multilingual.faker:multilingual_sample_provider'],
 'oarepo_model_builder.templates': ['100-multilingual_templates = '
                                    'oarepo_model_builder_multilingual.invenio']}

setup_kwargs = {
    'name': 'oarepo-model-builder-multilingual',
    'version': '0.2.4',
    'description': '',
    'long_description': '# OARepo Model Builder Multilingual\n\n',
    'author': 'Alzbeta Pokorna',
    'author_email': 'alzbeta.pokorna@cesnet.cz',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
