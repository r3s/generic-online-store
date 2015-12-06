# from django.db import models
# from django.contrib.auth.models import User
# from django.conf import settings
# import logging
#
# #globals
# if not Settings.DEBUG:
#     logger = logging.getLogger("django.request")
# else:
#     logger = logging.getLogger("gs_file")

#FUTURE
"""
 class UserWishlist(models.Model):
     pass
 class UserReview(models.Model):
     pass

"customer_communicationeventtype" (
        "code" varchar(128) NOT NULL UNIQUE,
        "name" varchar(255) NOT NULL,
        "category" varchar(255) NOT NULL,
        "email_subject_template" varchar(255) NULL,
        "email_body_template" text NULL,
        "email_body_html_template" text NULL,
        "sms_template" varchar(170) NULL,
        "date_created" datetime NOT NULL,
        "date_updated" datetime NOT NULL);

"customer_email" (
        "subject" text NOT NULL,
        "body_text" text NOT NULL,
        "body_html" text NOT NULL,
        "date_sent" datetime NOT NULL,
        "user_id" integer NOT NULL REFERENCES "auth_user" ("id"));

"customer_notification" (
        "subject" varchar(255) NOT NULL,
        "body" text NOT NULL,
        "category" varchar(255) NOT NULL,
        "location" varchar(32) NOT NULL,
        "date_sent" datetime NOT NULL,
        "date_read" datetime NULL,
        "recipient_id" integer NOT NULL REFERENCES "auth_user" ("id"),
        "sender_id" integer NULL REFERENCES "auth_user" ("id"));

"customer_productalert" (
        "email" varchar(75) NOT NULL,
        "key" varchar(128) NOT NULL,
        "status" varchar(20) NOT NULL,
        "date_created" datetime NOT NULL,
        "date_confirmed" datetime NULL,
        "date_cancelled" datetime NULL,
        "date_closed" datetime NULL,
        "product_id" integer NOT NULL REFERENCES "catalogue_product" ("id"),
        "user_id" integer NULL REFERENCES "auth_user" ("id"));
"""
