const Configuration = {
    parserPreset: {
      parserOpts: { headerPattern: /^([^\(\):]*)(?:\((.*)\))?!?: (.*)$/ }
    },
    /*
     * Resolve and load @commitlint/config-conventional from node_modules.
     * Referenced packages must be installed
     */
    extends: ['@commitlint/config-conventional'],
    rules: {
      'type-enum': [
        2,
        'always',
        [
          'build',
          'chore',
          'ci',
          'docs',
          'feat',
          'fix',
          'perf',
          'refactor',
          'revert',
          'style',
          'test'
        ]
      ]
    }
  }
  
  
  module.exports = Configuration