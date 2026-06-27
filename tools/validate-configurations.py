#!/usr/bin/env python3
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / 'configuration-examples'
CONFIGS = sorted(CONFIG_DIR.glob('*.configuration.yaml'))
STAGE_DEFAULTS = {f'stage-{i}-default.configuration.yaml' for i in range(1, 5)}
PROMPT_MODES = {
    'stage_1': {'no_questions_full_ai_design_fabrication','low_stakes_design_interview','medium_stakes_design_interview','high_stakes_design_interview'},
    'stage_2': {'no_questions_full_ai_execution_planning','low_stakes_execution_interview','medium_stakes_execution_interview','high_stakes_execution_interview'},
    'stage_3': {'no_questions_full_ai_fabrication','low_stakes_fabrication_interview','medium_stakes_fabrication_interview','high_stakes_fabrication_interview'},
    'stage_4': {'no_questions_full_ai_validation_packaging','low_stakes_finalization_interview','medium_stakes_finalization_interview','high_stakes_finalization_interview'},
}
BASE_REQUIRED = {'configuration_metadata','prompt_mode','stage_authority','configuration_priority','output_suite','artifact_boundary_markers','required_document_tree','document_headers','machine_readable_companions','completion_gate','status'}
PROFILE_REQUIRED = {'configuration_metadata','prompt_mode','stage_authority','configuration_priority','output_suite','artifact_boundary_markers','required_document_tree','document_headers','status'}
errors = []

PROFILE_DEPTH_REQUIRED_KEYS = {
    'web_application': {
        'stage_1': ['web_application_profile_depth', 'web_frontend_design', 'web_backend_and_data_design', 'web_security_privacy_design'],
        'stage_2': ['web_application_execution_profile_depth', 'web_expected_artifacts', 'web_work_package_rules'],
        'stage_3': ['web_application_fabrication_profile_depth', 'web_text_file_fabrication', 'web_external_validation_handling'],
        'stage_4': ['web_application_finalization_profile_depth', 'web_validation_scope', 'web_final_handoff_rules'],
    },
    'shared_library': {
        'stage_1': ['shared_library_profile_depth', 'library_api_design', 'library_packaging_design'],
        'stage_2': ['shared_library_execution_profile_depth', 'library_expected_artifacts', 'library_work_package_rules'],
        'stage_3': ['shared_library_fabrication_profile_depth', 'library_text_file_fabrication', 'library_external_validation_handling'],
        'stage_4': ['shared_library_finalization_profile_depth', 'library_validation_scope', 'library_final_handoff_rules'],
    },
}


def load(path: Path):
    try:
        data = yaml.safe_load(path.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'{path.relative_to(ROOT)}: YAML parse error: {exc}')
        return None
    if not isinstance(data, dict):
        errors.append(f'{path.relative_to(ROOT)}: expected mapping at root')
        return None
    return data

for rel in ['pipeline.configuration.yaml','configuration-examples/configuration-index.yaml','configuration-examples/profile-family-roadmap.yaml']:
    path = ROOT / rel
    if not path.exists():
        errors.append(f'Missing configuration support file: {rel}')
    else:
        load(path)

for path in CONFIGS:
    data = load(path)
    if data is None:
        continue
    rel = path.relative_to(ROOT).as_posix()
    meta = data.get('configuration_metadata') or {}
    stage = meta.get('applies_to_stage')
    if stage not in PROMPT_MODES:
        errors.append(f'{rel}: invalid or missing configuration_metadata.applies_to_stage')
    selected = (data.get('prompt_mode') or {}).get('selected_mode')
    if stage in PROMPT_MODES and selected not in PROMPT_MODES[stage]:
        errors.append(f'{rel}: invalid selected_mode {selected!r} for {stage}')
    required = BASE_REQUIRED if path.name in STAGE_DEFAULTS else PROFILE_REQUIRED
    missing = sorted(k for k in required if k not in data)
    if missing:
        errors.append(f'{rel}: missing required top-level keys: {missing}')
    if path.name not in STAGE_DEFAULTS and not meta.get('extends'):
        errors.append(f'{rel}: product-specific profile should declare configuration_metadata.extends')

    profile = meta.get('product_type_profile')
    if profile in PROFILE_DEPTH_REQUIRED_KEYS and stage in PROFILE_DEPTH_REQUIRED_KEYS[profile]:
        for key in PROFILE_DEPTH_REQUIRED_KEYS[profile][stage]:
            if key not in data:
                errors.append(f'{rel}: missing Batch 12 profile-depth key {key!r}')
    text = path.read_text(encoding='utf-8')
    if '\t' in text:
        errors.append(f'{rel}: contains tab characters')
    if not any(term in text for term in ['do_not','preserve','review','placeholder','authorization','external_validation','external_tool']):
        errors.append(f'{rel}: missing safety/review/placeholder language')

for stage in range(1, 5):
    schema = ROOT / 'schemas' / f'stage-{stage}-configuration.schema.yaml'
    data = load(schema)
    if data is None:
        continue
    if 'schema_inheritance_policy' not in data:
        errors.append(f'{schema.relative_to(ROOT)}: missing schema_inheritance_policy')
    if 'required_explicit_top_level_keys' not in data:
        errors.append(f'{schema.relative_to(ROOT)}: missing required_explicit_top_level_keys')

if errors:
    print('Configuration validation failed:')
    for e in errors:
        print('-', e)
    sys.exit(1)
print(f'Configuration validation passed. Checked {len(CONFIGS)} stage configuration files plus support configuration files.')
