from .models import TaskLog

def filter_tasks_by_params(params, workspace_id: int):
    task_status = params.get('status').split(',')
    expense_group_ids = params.get('expense_group_ids')
    task_type = params.get('task_type').split(',')

    filters = {
        'workspace_id': workspace_id,
        'status__in': task_status,
        'type__in': task_type
    }

    if expense_group_ids:
        expense_group_ids = expense_group_ids.split(',')
        filters['expense_group_id__in'] = expense_group_ids

    return TaskLog.objects.filter(**filters).order_by('-updated_at').all()
