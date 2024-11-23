import graphene
from graphene_django import DjangoObjectType
from applications.kanban.models import Column, Task


class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = ('id', 'description', 'status', 'created_at')


class ColumnType(DjangoObjectType):
    tasks = graphene.List(TaskType)

    class Meta:
        model = Column
        fields = ('id', 'name', 'tasks')

    def resolve_tasks(self, info):
        return self.tasks.all()


class Query(graphene.ObjectType):
    all_data_in_columns = graphene.List(ColumnType)

    def resolve_all_data_in_columns(self, info):
        return Column.objects.prefetch_related('tasks').all()


class CreateTask(graphene.Mutation):
    class Arguments:
        description = graphene.String(required=True)
        status = graphene.String()
        column = graphene.Int(required=True)

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, info, description, status, column):
        column = Column.objects.get(id=column)
        task = Task.objects.create(description=description,
                                   status=status,
                                   column=column)
        task.save()
        return CreateTask(task=task)


class UpdateTask(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        description = graphene.String()
        status = graphene.String()
        column = graphene.Int()

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, root, info, id, description=None, status=None, column=None):
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            raise Exception(f"Task does not exists")

        if description is not None:
            task.description = description
        if status is not None:
            task.status = status
        if column is not None:
            try:
                column_instance = Column.objects.get(id=column)
                task.column = column_instance
            except Column.DoesNotExist:
                raise Exception(f"column does not exists")
        task.save()
        return UpdateTask(task=task)


class DeleteTask(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    task = graphene.Field(TaskType)

    @classmethod
    def mutate(cls, root, info, id):
        try:
            task = Task.objects.get(id=id)
            task.delete()
        except Task.DoesNotExist:
            raise Exception(f"Task does not exists")


class CreateColumn(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)

    column = graphene.Field(ColumnType)

    @classmethod
    def mutate(cls, root, info, name):
        column = Column.objects.create(name=name)
        column.save()
        return CreateColumn(column=column)


class UpdateColumn(graphene.Mutation):

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)

    column = graphene.Field(ColumnType)

    @classmethod
    def mutate(cls, root, info, name, id):
        column = Column.objects.get(id=id)
        column.name = name
        column.save()
        return UpdateColumn(column=column)


class DeleteColumn(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    column = graphene.Field(ColumnType)

    @classmethod
    def mutate(cls, root, info, id):
        column = Column.objects.get(id=id)
        column.delete()
        return


class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()
    update_task = UpdateTask.Field()
    delete_task = DeleteTask.Field()

    update_column = UpdateColumn.Field()
    delete_column = DeleteColumn.Field()
    create_column = CreateColumn.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
