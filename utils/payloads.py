

create_booking_payload={
    "firstname" : "Michael",
    "lastname" : "Scofield",
    "totalprice" : 222,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }

auth_payload={
    "username" : "admin",
    "password" : "password123"
    }

update_booking_payload={
    "firstname" : "Michael-updated",
    "lastname" : "Scofield-updated",
    "totalprice" : 555,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-02-02",
        "checkout" : "2019-02-02"
    },
    "additionalneeds" : "Lunch"
    }

partial_update_payload={
    "firstname" : "Michael-updated",
    "additionalneeds" : "Lunch"
    }
