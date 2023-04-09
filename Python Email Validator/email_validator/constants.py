import re

# Maximum Length of Email Address
EMAIL_MAX_LENGTH = 254  #(IETF) RFC 5321.
LOCAL_PART_MAX_LENGTH = 64  #  RFC 5321
DOMAIN_MAX_LENGTH = 255  # (according to RFC 1035 and RFC 5321)
DNS_LABEL_LENGTH_LIMIT = 63  # in "octets", RFC 1035 2.3.1


pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
pattern = re.compile(pattern)
