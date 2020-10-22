from authnapp.forms import ShopUserEditForm
from authnapp.models import ShopUser


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = "__all__"