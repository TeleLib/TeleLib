/* eslint-disable indent */
module.exports = {
    'ignorePatterns': ['dist/*'],
    'env': {
        browser: true,
        node: true,
        es2021: true
    },
    'extends': [
        'eslint:recommended',
        'plugin:@typescript-eslint/recommended'
    ],
    'parser': '@typescript-eslint/parser',
    'parserOptions': {
        'ecmaVersion': 'latest',
        'sourceType': 'module'
    },
    'plugins': [
        '@typescript-eslint',
        'unused-imports'
    ],
    'rules': {
        '@typescript-eslint/no-explicit-any': 'off',
        'no-unused-vars': 'off',
        'unused-imports/no-unused-imports': 'error',
        'unused-imports/no-unused-vars': [
            'warn',
            {
                'vars': 'all',
                'varsIgnorePattern': '^_',
                'args': 'after-used',
                'argsIgnorePattern': '^_'
            }
        ],
        'indent': [
            'error',
            'tab'
        ],
        'linebreak-style': [
            'error',
            'unix'
        ],
        'quotes': [
            'error',
            'single'
        ],
        'semi': [
            'error',
            'never'
        ]
    }
}