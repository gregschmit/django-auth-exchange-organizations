from django.db import models
from organizations.models import Organization
from .settings import get_setting


class DomainOrganization(models.Model):
    """
    Association between a domain and an organization. Multiple associations are
    reasonable, e.g., "example.com" and "EXAMPLE" might both point to the same
    organization, so that would require two entries here.
    """
    domain = models.CharField(max_length=255, unique=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def associate_new_user(cls, user, domain):
        """
        If AUTH_EXCHANGE_ORGS_AUTOASSOCIATE is True, then try to find a
        DomainOrganization to add this user to. If you cannot find one, then if
        AUTH_EXCHANGE_ORGS_AUTO_CREATE_ORGS is True, then create an Organization
        and DomainOrganization and add the user to it.
        """
        if get_setting('AUTH_EXCHANGE_ORGS_AUTOASSOCIATE'):
            try:
                d = DomainOrganization.objects.get(domain=domain)
            except DomainOrganization.DoesNotExist:
                d = None
            if d:
                d.organization.add_user(user)
            else:
                if get_setting('AUTH_EXCHANGE_ORGS_AUTO_CREATE_ORGS'):
                    o, created = Organization.objects.get_or_create(name=domain)
                    d = DomainOrganization.objects.create(domain=domain, organization=o)
                    o.add_user(user)
