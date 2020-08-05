from django_filters import rest_framework as filters

from home.models import AxfGoods


class GoodsFilter(filters.FilterSet):
    typeid = filters.CharFilter(field_name='categoryid', lookup_expr='exact')
    childcid = filters.CharFilter(field_name='childcid', method='filter_child_type')
    order_rule = filters.CharFilter(field_name='order_rule', method='order_goods')
    class Meta:
        model = AxfGoods
        fields = ['categoryid']

    def filter_child_type(self, queryset, mame, value):
        if int(value) > 0:  # 当value大于0，要进行子类过滤
            return queryset.filter(childcid=int(value))
        # 如果value为0，则没有子类
        return queryset

    def order_goods(self, queryset, name, value):
        value = int(value)
        if value == 1:
            queryset = queryset.order_by("price")
        elif value == 2:
            queryset = queryset.order_by("-price")
        elif value == 3:
            queryset = queryset.order_by("productnum")
        elif value == 4:
            queryset = queryset.order_by("-productnum")

        return queryset