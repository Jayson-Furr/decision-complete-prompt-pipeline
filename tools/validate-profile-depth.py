#!/usr/bin/env python3
"""Validate product-profile depth coverage for public v1.0.0 profiles."""
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / 'configuration-examples'

def norm(text: str) -> str:
    return re.sub(r'[^a-z0-9]+', '_', text.lower()).strip('_')

PROFILE_REQUIREMENTS = {
    'web-application': {
        1: ['web_application_design_profile', 'hidden_design_decision_scan'],
        2: ['web_application_execution_profile', 'hidden_execution_decision_scan'],
        3: ['web_application_fabrication_profile', 'hidden_fabrication_decision_scan'],
        4: ['web_application_finalization_profile', 'hidden_finalization_decision_scan'],
        'family_keywords': ['authentication', 'authorization', 'personal data', 'deployment', 'accessibility', 'external validation'],
    },
    'shared-library': {
        1: ['shared_library_design_profile', 'hidden_design_decision_scan'],
        2: ['shared_library_execution_profile', 'hidden_execution_decision_scan'],
        3: ['shared_library_fabrication_profile', 'hidden_fabrication_decision_scan'],
        4: ['shared_library_finalization_profile', 'hidden_finalization_decision_scan'],
        'family_keywords': ['public api', 'versioning', 'compatibility', 'package', 'license', 'registry'],
    },
    'unity-game': {
        1: ['unity_toolchain', 'unity_design_surface_coverage'],
        2: ['unity_work_package_generation', 'unity_external_validation_planning'],
        3: ['unity_fabrication_scope', 'unity_environment_detection'],
        4: ['unity_validation_scope', 'unity_final_package'],
        'family_keywords': ['unity', 'external validation', 'external tool', 'rights', 'build'],
    },
}

errors = []
for family, req in PROFILE_REQUIREMENTS.items():
    combined_text = ''
    for stage in range(1, 5):
        path = CONFIG / f'stage-{stage}-{family}.configuration.yaml'
        if not path.exists():
            errors.append(f'Missing profile file: {path.relative_to(ROOT)}')
            continue
        raw = path.read_text(encoding='utf-8')
        combined_text += '\n' + raw
        try:
            data = yaml.safe_load(raw)
        except Exception as exc:
            errors.append(f'{path.relative_to(ROOT)}: YAML parse error: {exc}')
            continue
        if not isinstance(data, dict):
            errors.append(f'{path.relative_to(ROOT)}: root must be a mapping')
            continue
        for key in req[stage]:
            if key not in data:
                errors.append(f'{path.relative_to(ROOT)}: missing product-depth key {key!r}')
        metadata = data.get('configuration_metadata') or {}
        if family in {'web-application', 'shared-library'} and metadata.get('profile_depth_status') != 'deepened_v1_0_0_batch_12':
            errors.append(f'{path.relative_to(ROOT)}: missing profile_depth_status marker')
    normalized_family_text = norm(combined_text)
    for keyword in req['family_keywords']:
        if norm(keyword) not in normalized_family_text:
            errors.append(f'Profile family {family}: expected profile-depth keyword {keyword!r}')

if errors:
    print('Profile depth validation failed:')
    for error in errors:
        print('-', error)
    sys.exit(1)
print('Profile depth validation passed. Web application and shared-library profiles include deepened Stage 1-4 profile blocks; Unity profile remains deep.')
