class Image {
    constructor(id, source, displayed, timeout) {
        this.id = id;
        this.source = source;
        this.displayed = displayed;
        this.timeout = timeout
    }

    get id() {
        return this._id;

    }

    get source() {
        return this._source;
    }


    get displayed() {
        return this._displayed;
    }

    get timeout() {
        return this._timeout;
    }

    set id(value) {
        this._id = value;

    }

    set source(value) {
        this._source = value;
    }


    set displayed(value) {
        this._displayed = value
    }

    set timeout(value) {
        this._timeout = value
    }
}


const images = [
    new Image(1, "static/images/PasswordImages/1.JPG", true, 5),
    new Image(2, "static/images/PasswordImages/2.JPG", true, 5),
    new Image(3, "static/images/PasswordImages/3.JPG", true, 5),
    new Image(4, "static/images/PasswordImages/4.JPG", true, 5),
    new Image(5, "static/images/PasswordImages/5.JPG", true, 5),
    new Image(6, "static/images/PasswordImages/6.JPG", true, 5),
    new Image(7, "static/images/PasswordImages/7.JPG", false, 5),
    new Image(8, "static/images/PasswordImages/8.JPG", false, 5),
    new Image(9, "static/images/PasswordImages/9.JPG", false, 5),
    new Image(10, "static/images/PasswordImages/10.JPG", false, 5),
    new Image(11, "static/images/PasswordImages/11.JPG", false, 5),
    new Image(12, "static/images/PasswordImages/12.JPG", false, 5),
    new Image(13, "static/images/PasswordImages/13.JPG", false, 5),
    new Image(14, "static/images/PasswordImages/14.JPG", false, 5),
    new Image(15, "static/images/PasswordImages/15.JPG", false, 5),
    new Image(16, "static/images/PasswordImages/16.JPG", false, 5),
    new Image(17, "static/images/PasswordImages/17.JPG", false, 5),
    new Image(18, "static/images/PasswordImages/18.JPG", false, 5),
    new Image(19, "static/images/PasswordImages/19.JPG", false, 5),
    new Image(20, "static/images/PasswordImages/20.JPG", false, 5),
    new Image(21, "static/images/PasswordImages/21.JPG", false, 5),
    new Image(22, "static/images/PasswordImages/22.JPG", false, 5),
    new Image(23, "static/images/PasswordImages/23.JPG", false, 5),
    new Image(24, "static/images/PasswordImages/24.JPG", false, 5),
    new Image(25, "static/images/PasswordImages/25.JPG", false, 5),
    new Image(26, "static/images/PasswordImages/26.JPG", false, 5),
    new Image(27, "static/images/PasswordImages/27.JPG", false, 5),
    new Image(28, "static/images/PasswordImages/28.JPG", false, 5),
    new Image(29, "static/images/PasswordImages/29.JPG", false, 5),
    new Image(30, "static/images/PasswordImages/30.JPG", false, 5),
    new Image(31, "static/images/PasswordImages/31.JPG", false, 5),
    new Image(32, "static/images/PasswordImages/32.JPG", false, 5),
    new Image(33, "static/images/PasswordImages/33.JPG", false, 5),
    new Image(34, "static/images/PasswordImages/34.JPG", false, 5),
    new Image(35, "static/images/PasswordImages/35.JPG", false, 5),
    new Image(36, "static/images/PasswordImages/36.JPG", false, 5),
    new Image(37, "static/images/PasswordImages/37.JPG", false, 5),
    new Image(38, "static/images/PasswordImages/38.JPG", false, 5),
    new Image(39, "static/images/PasswordImages/39.JPG", false, 5),
    new Image(40, "static/images/PasswordImages/40.JPG", false, 5),


];


function refresh_images() {
    var displayedImages = document.getElementsByClassName("password_image");
    var imageHTMLValue = document.getElementsByClassName("password_image_value");
    let freshImages = images.filter(x => x.displayed === false);

    for (let current_image = 0; current_image < displayedImages.length; current_image++) {
        let x = imageHTMLValue[current_image].value;
        x = x.replace(".jpg", "");
        x = parseInt(x);
        images[x].displayed = false;
    }

    let selected_image = 0;
    while (selected_image < 6) {
        var randomInt = getRandomInt(0, freshImages.length - 1);
        if (!freshImages[randomInt].displayed) {
            freshImages[randomInt].displayed = true;
            displayedImages[selected_image] = freshImages[randomInt].id;

            displayedImages[selected_image].src = freshImages[randomInt].source;
            displayedImages[selected_image].src = displayedImages[selected_image].src.replace("http://" + ip_port + "/selected_user", "");
            imageHTMLValue[selected_image].value = images[randomInt].id + ".JPG";
            selected_image++;
        }
    }
}

