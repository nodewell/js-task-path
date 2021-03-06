'use strict';

/**
 * @namespace js.task.path.exception
 */

const Exception = require('js-lang-exception');

/**
 * Exception ID.
 *
 * @private
 * @const {number} ID
 */
const ID = 1001;

/**
 * Exception, when the glob must be a string or an array.
 *
 * @class InvalidGlobException
 * @memberOf js.task.path.exception
 */
module.exports = class InvalidGlobException extends Exception {

    constructor(glob) {
        const type = typeof glob;

        super(`Invalid glob, the glob most be a string or an array, got: "${type}"`, ID);
    }
};
