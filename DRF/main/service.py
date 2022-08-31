def lol(models):
    for model in models:
        del_list = model.objects.filter(is_active=False)
        print(del_list)
        del_list.delete()
