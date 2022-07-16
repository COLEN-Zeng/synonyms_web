const path = require('path');
const fs = require('fs');

const ENV = 'dev';
const PROJECT_ROOT = `${__dirname}/../../..`;
const PROJECT_NAME = require('../../../package.json').name;
const NAME_PREFIX = `${ENV}/${PROJECT_NAME}/`;

const HOST = `backend-${PROJECT_NAME}`;
const PORT = 8001;

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
    },
);

module.exports = {
    apps,
};
