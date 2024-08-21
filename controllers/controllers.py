from odoo.addons.portal.controllers.portal import CustomerPortal

class PortalCont(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        """Values for /my & /my/home routes template rendering.

        Includes the record count for the displayed badges.
        where 'coutners' is the list of the displayed badges
        and so the list to compute.
        """
        rtn = super(PortalCont, self)._prepare_home_portal_values(counters)
        return rtn