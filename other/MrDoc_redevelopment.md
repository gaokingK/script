### BUG
> 下面的两种情况将会导致改变含子文档的文档的status改变后，预期的改变将会溢出
    1. 开发的create_doc API 可能把3级文档作为父级文档，这样将导致前端的文档树上不显示该文档。
    2. 原始代码有子文档的status如果为删除状态，子文档也会一起删除，改变为草稿状态的话，将会导致子文档不能文档树上显示。
### 部署
1. mrdoc.sh
    ```
    #!/bin/sh
    python /usr/src/app/manage.py makemigrations && python /usr/src/app/manage.py migrate && echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'example@fuck.com', 'password')" | python /usr/src/app/manage.py shell
    python -u /usr/src/app/manage.py runserver --noreload 0.0.0.0:${LISTEN_PORT}
    exec "$@"

    ```