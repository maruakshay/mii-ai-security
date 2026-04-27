# Adversarial Fixtures

This directory contains canonical prompt-injection fixtures for repeatable testing.

## Standard Format

Each fixture is a single JSON object with these required fields:

- `id`
- `title`
- `category`
- `attack_surface`
- `prompt`
- `expected_behavior`
- `tags`

## Usage

- Treat each fixture as untrusted input.
- Run fixtures against preprocessing, policy, retrieval, tool-routing, and output-validation layers.
- Add new fixtures when a real bypass is found or when a control changes.
