from rest_framework.pagination import PageNumberPagination

class SpecificationInfoSetPagination(PageNumberPagination):
	# 默认每页显示的数据条数
	page_size = 5
	# 获取URL参数中设置的每页显示数据条数
	page_size_query_param = 'page_size'
	# 获取URL参数中传入的页码key
	page_query_param = 'page'
