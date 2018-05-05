from flask import request

def pagination_from_request(sort, order, page, perpage):
	pagination = {
		'sort': sort,
		'order': order,
		'page': page,
		'perpage': perpage,
	}
	if 'sort' in request.args:
		pagination['sort'] = request.args['sort']
	if 'order' in request.args:
		pagination['order'] = request.args['order']
	if 'page' in request.args:
		pagination['page'] = int(request.args['page'])
	if 'perpage' in request.args and request.args['perpage'] and 0 < int(request.args['perpage']):
		pagination['perpage'] = int(request.args['perpage'])

	return pagination
