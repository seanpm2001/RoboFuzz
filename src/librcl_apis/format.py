s = """\
rcl_get_zero_initialized_publisher
rcl_publisher_init
rcl_publisher_fini
rcl_publisher_get_default_options
rcl_borrow_loaned_message
rcl_return_loaned_message_from_publisher
rcl_publish
rcl_publish_serialized_message
rcl_publish_loaned_message
rcl_publisher_assert_liveliness
rcl_publisher_get_topic_name
rcl_publisher_get_options
rcl_publisher_get_rmw_handle
rcl_publisher_get_context
rcl_publisher_is_valid
rcl_publisher_is_valid_except_context
rcl_publisher_get_subscription_count
rcl_publisher_get_actual_qos
rcl_publisher_can_loan_messages"""


ss = ""
for a in s.split("\n"):
    ss += " -x " + a + "@librcl.so"

print(ss)

