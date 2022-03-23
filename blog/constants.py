POST_STATUS_CHOICES = (
    ('PUBLISHED', 'published'), # viewable by everyone
    ('FUTURE', 'future'), # scheduled to be published in a future date
    ('DRAFT', 'draft'), # incomplete post viewable only in admin
    ('BINNED', 'binned'), # posts in the bin
)

COMMENT_STATUS_CHOICES = (
    ('APPROVED', 'approved'), # approved and visible to everyone
    ('DISAPPROVED', 'disapproved'), # not approved for whatever reason
    ('PENDING', 'pending'), # awaiting approval by an admin
    ('FLAGGED_AS_INAPPROPRIATE', 'flagged_as_inappropriate'), # this has been flagged as inappropriate
)