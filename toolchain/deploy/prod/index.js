const path = require('path');
const fs = require('fs');

const ENV = 'prod';
const PROJECT_ROOT = `${__dirname}/../../..`;
const PROJECT_NAME = require('../../../package.json').name;
const NAME_PREFIX = `${ENV}/${PROJECT_NAME}/`;

const HOST = `backend-${PROJECT_NAME}`;
const PORT = 8001;

const GIT_BRANCH = 'master';
const REMOTE_ROOT = '/home/{user}/synonyms_web';// TODO:
const SSH_USER = '';
const SSH_HOST = '';
const SSH_PORT =

let apps = [].concat(
    {
        namePrefix: NAME_PREFIX,
        name: 'basic',
        // script: `${PROJECT_ROOT}/node_modules/.bin/registry_service`,
        script: `${PROJECT_ROOT}/main.py`,
        args: {
            // 'log-path': `${PROJECT_ROOT}/logs/basic/registry`,
            "interpreter": "python3",
            host: HOST,
            port: PORT,
        },
        env: { ENV, TZ: 'Asia/Shanghai' },
        // nodeArgs: {
        //     'max-old-space-size': '4096',
        // },
        watch: []
    },
);

module.exports = {
    apps,
    deploy: {
        user: SSH_USER,
        host: SSH_HOST,
        sshPort: SSH_PORT,
        localRoot: PROJECT_ROOT,
        remoteRoot: REMOTE_ROOT,
        exclude: [
            '.git',
            'logs',
            '.vscode',
            'venv'
        ],
        hook: {
            preLocal: [
                `cd ${PROJECT_ROOT} && yarn`,
                `cd ${PROJECT_ROOT} && git checkout . && git checkout ${GIT_BRANCH} && git pull origin ${GIT_BRANCH}`,
            ],
            afterRemote: [
                `cd ${REMOTE_ROOT} && ./run.sh ${ENV}`,
            ],
        },
    },
};
