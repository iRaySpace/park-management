# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "park_management"
app_title = "Park Management"
app_publisher = "9T9IT"
app_description = "ERPNext App for managing park"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@9t9it.com"
app_license = "MIT"

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Customer-pm_children_allowed",
                    "Customer-pm_adults_allowed",
                    "Customer-pm_lease_validity",
                    "Customer-pm_customer_cb",
                    "Customer-pm_city",
                    "Customer-pm_building_no",
                    "Customer-pm_building_name",
                    "Customer-pm_cpr_expiry_date",
                    "Customer-pm_country",
                    "Customer-pm_area_name",
                    "Customer-pm_road_name",
                    "Customer-pm_road_no",
                    "Customer-pm_flat_no",
                    "Customer-pm_property_card_no",
                    "Customer-pm_cpr_no",
                    "Customer-pm_customer_sb",
                    "Customer-pm_vehicle_no"
                ]
            ]
        ]
    }
]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/park_management/css/park_management.css"
# app_include_js = "/assets/park_management/js/park_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/park_management/css/park_management.css"
# web_include_js = "/assets/park_management/js/park_management.js"

# include js in page
page_js = {"pos": "public/js/pos.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "park_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "park_management.install.before_install"
# after_install = "park_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "park_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"park_management.tasks.all"
# 	],
# 	"daily": [
# 		"park_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"park_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"park_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"park_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "park_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "park_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "park_management.task.get_dashboard_data"
# }
