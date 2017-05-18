
function initialize() {

    //Map parametrs
    var mapOptions_place = {
        zoom: 10,
        center: new google.maps.LatLng(41.154, -73.328),
        mapTypeId: google.maps.MapTypeId.ROADMAP,

        mapTypeControl: false,
        mapTypeControlOptions: {
            style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR,
            position: google.maps.ControlPosition.BOTTOM_CENTER
        },
        panControl: false,
        panControlOptions: {
            position: google.maps.ControlPosition.TOP_RIGHT
        },
        zoomControl: false,
        zoomControlOptions: {
            style: google.maps.ZoomControlStyle.LARGE,
            position: google.maps.ControlPosition.TOP_RIGHT
        },
        scaleControl: false,
        scaleControlOptions: {
            position: google.maps.ControlPosition.TOP_LEFT
        },
        streetViewControl: false,
        streetViewControlOptions: {
            position: google.maps.ControlPosition.LEFT_TOP
        },
                styles: [{"featureType":"poi","stylers":[{"visibility":"off"}]},{"stylers":[{"saturation":-70},{"lightness":37},{"gamma":1.15}]},{"elementType":"labels","stylers":[{"gamma":0.26},{"visibility":"off"}]},{"featureType":"road","stylers":[{"lightness":0},{"saturation":0},{"hue":"#ffffff"},{"gamma":0}]},{"featureType":"road","elementType":"labels.text.stroke","stylers":[{"visibility":"off"}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"lightness":20}]},{"featureType":"road.highway","elementType":"geometry","stylers":[{"lightness":50},{"saturation":0},{"hue":"#ffffff"}]},{"featureType":"administrative.province","stylers":[{"visibility":"on"},{"lightness":-50}]},{"featureType":"administrative.province","elementType":"labels.text.stroke","stylers":[{"visibility":"off"}]},{"featureType":"administrative.province","elementType":"labels.text","stylers":[{"lightness":20}]}]
            };

    //map
    var map_place = new google.maps.Map(document.getElementById("map_place"), mapOptions_place);

    //category
    var Bank_place = 'img/icon/Bank.png';
    var Cafe_place = 'img/icon/Cafe.png';
    var Cinema_place = 'img/icon/Cinema.png';
    var Club_place = 'img/icon/Club.png';
    var Park_place = 'img/icon/Park.png';
    var Port_place = 'img/icon/Port.png';
    var Post_place = 'img/icon/Post.png';
    var Shop_place = 'img/icon/Shop.png';
    var Showplace_place = 'img/icon/Showplace.png';
    var Sport_place = 'img/icon/Sport.png';

    //positions
    var point_place = new google.maps.LatLng(41.154, -73.328);

    //markers
    var marker_place = className = 'Cafe';
    var marker_place = new google.maps.Marker({
        position: point_place,
        map: map_place,
        category: Cafe_place,
        icon: Cafe_place,
        title: "point_place"
    });
};

    
    