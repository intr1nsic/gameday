from gameday.models import University, League, Schedule
from django.contrib import admin

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'league', 'game_time', 'status', 'winteam', 'loseteam',)
    list_filter = ['league', 'status',]
    search_fields = ['winteam__name', 'loseteam__name',]
    order_by = '-game_time'
    list_per_page = 20
    save_as = True
    save_on_top = True

admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(University)
admin.site.register(League)