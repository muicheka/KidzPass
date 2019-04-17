const currentRecord = 0;

class Record {
    constructor(id, regStartTime, regEndTime, loginStartTime, loginEndTime, failedAttempts, successfulAttempts) {
        this.id = id;
        this.regStartTime = regStartTime;
        this.regEndTime = regEndTime;
        this.loginStartTime = loginStartTime;
        this.loginEndTime = loginEndTime;
        this.failedAttempts = failedAttempts;
        this.successfulAttempts = successfulAttempts;
    }

    get id() {
        return this._id;
    }

    get regStartTime() {
        return this._regStartTime
    }

    get regEndTime() {
        return this._regEndTime
    }

    get loginStartTime() {
        return this._loginStartTime
    }

    get loginEndTime() {
        return this._loginEndTime
    }

    get failedAttempts() {
        return this._failedAttempts
    }

    get successfulAttempts() {
        return this._successfulAttempts
    }

    set id(value) {
        this._id = value;
    }

    set regStartTime(value) {
        this._regStartTime = value;
    }

    set regEndTime(value) {
        this._regEndTime = value;
    }

    set loginStartTime(value) {
        this._loginStartTime = value;
    }

    set loginEndTime(value) {
        this._loginEndTime = value;
    }

    set failedAttempts(value) {
        this._failedAttempts = value;
    }

    set successfulAttempts(value) {
        this._successfulAttempts = value;
    }
}

var records = [
    new Record(0, "", "", "", "", 0, 0),
    new Record(1, "", "", "", "", 0, 0),
];

