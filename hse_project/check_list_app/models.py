from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Direction(models.Model):
    name = models.CharField(_('Direction/Subcontractor name'), max_length=25)

    def __str__(self) -> str:
        return self.name
    


class Car(models.Model):
    number = models.CharField(_('Plate number'), max_length=10)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.number
    
class CheckList(models.Model):
    CHOICES = [
        (1, _('YES')),
        (0, _('NO')),
        (2,_('N/A')),
    ]
    
    date = models.DateField(_('Date'))
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    driver = models.CharField(_('Driver_name'), max_length=25)
    fuel_mark = models.IntegerField(choices=CHOICES)
    fuel_comment = models.CharField(_('Comment'), max_length=40)
    # next step
    oil_mark = models.IntegerField(choices=CHOICES)
    oil_comment = models.CharField(_('Comment'), max_length=40)
    brake_fluid_mark = models.IntegerField(choices=CHOICES)
    brake_fluid_comment = models.CharField(_('Comment'), max_length=40)
    cooling_fluid_mark = models.IntegerField(choices=CHOICES)
    cooling_fluid_comment = models.CharField(_('Comment'), max_length=40)
    windshield_fluid_mark = models.IntegerField(choices=CHOICES)
    windshield_fluid_comment = models.CharField(_('Comment'), max_length=40)
    # next step
    headlights_mark = models.IntegerField(choices=CHOICES, default=None)
    headlights_comment = models.CharField(_('Comment'), max_length=40, default=None)
    revers_lights_mark = models.IntegerField(choices=CHOICES, default=None)
    revers_lights_comment = models.CharField(_('Comment'), max_length=40, default=None)
    turn_stop_ind_mark = models.IntegerField(choices=CHOICES, default=None) 
    turn_stop_ind_comment = models.CharField(_('Comment'), max_length=40, default=None)
    # next step
    wheel_mark = models.IntegerField(choices=CHOICES, default=None)
    wheel_comment = models.CharField(_('Comment'), max_length=40, default=None)
    clutch_mark = models.IntegerField(choices=CHOICES, default=None)
    clutch_comment = models.CharField(_('Comment'), max_length=40, default=None)
    brake_mark = models.IntegerField(choices=CHOICES, default=None)
    brake_comment = models.CharField(_('Comment'), max_length=40, default=None)
    monitor_device_mark = models.IntegerField(choices=CHOICES, default=None)
    monitor_comment = models.CharField(_('Comment'), max_length=40, default=None)
    heater_cond_mark = models.IntegerField(choices=CHOICES, default=None)
    heater_cond_comment = models.CharField(_('Comment'), max_length=40, default=None)
    wipers_mark = models.IntegerField(choices=CHOICES, default=None)
    wipers_comment = models.CharField(_('Comment'), max_length=40, default=None)
    beep_mark = models.IntegerField(choices=CHOICES, default=None)
    beep_comment = models.CharField(_('Comment'), max_length=40, default=None)
    beep_reverse_mark = models.IntegerField(choices=CHOICES, default=None)
    beep_reverse_comment = models.CharField(_('Comment'), max_length=40, default=None)
    gps_mark = models.IntegerField(choices=CHOICES, default=None)
    gps_comment = models.CharField(_('Comment'), max_length=40, default=None)
    dvr_mark = models.IntegerField(choices=CHOICES, default=None)
    dvr_comment = models.CharField(_('Comment'), max_length=40, default=None)
    battery_mark = models.IntegerField(choices=CHOICES, default=None)
    battery_comment = models.CharField(_('Comment'), max_length=40, default=None)
    # next step
    inside_out_mark = models.IntegerField(choices=CHOICES, default=None)
    inside_out_comment = models.CharField(_('Comment'), max_length=40, default=None)
    mirrors_glass_mark = models.IntegerField(choices=CHOICES, default=None)
    mirrors_glass_comment = models.CharField(_('Comment'), max_length=40, default=None)
    seat_belts_mark = models.IntegerField(choices=CHOICES, default=None)
    seat_belts_comment = models.CharField(_('Comment'), max_length=40, default=None)
    tires_press_mark = models.IntegerField(choices=CHOICES, default=None)
    tires_press_comment = models.CharField(_('Comment'), max_length=40, default=None)
    disks_mark = models.IntegerField(choices=CHOICES, default=None)
    disks_comment = models.CharField(_('Comment'), max_length=40, default=None)
    number_mark = models.IntegerField(choices=CHOICES, default=None)
    number_comment = models.CharField(_('Comment'), max_length=40, default=None)
    wheel_nuts_mark = models.IntegerField(choices=CHOICES, default=None)
    wheel_nuts_comment = models.CharField(_('Comment'), max_length=40, default=None)
    # next step
    extingusher_mark = models.IntegerField(choices=CHOICES, default=None)
    extingusher_comment = models.CharField(_('Comment'), max_length=40, default=None)
    first_aid_kit_mark = models.IntegerField(choices=CHOICES, default=None)
    first_aid_kit_comment = models.CharField(_('Comment'), max_length=40, default=None)
    car_tools_mark = models.IntegerField(choices=CHOICES, default=None)
    car_tools_comment = models.CharField(_('Comment'), max_length=40, default=None)
    spare_wheel_mark = models.IntegerField(choices=CHOICES, default=None)
    spare_wheel_comment = models.CharField(_('Comment'), max_length=40, default=None)
    warning_triangle_mark = models.IntegerField(choices=CHOICES, default=None)
    warning_triangle_comment = models.CharField(_('Comment'), max_length=40, default=None)
    tow_rope_mark = models.IntegerField(choices=CHOICES, default=None)
    tow_rope_comment = models.CharField(_('Comment'), max_length=40, default=None)
    wheel_chocks_mark = models.IntegerField(choices=CHOICES, default=None)
    wheel_chocks_comment = models.CharField(_('Comment'), max_length=40, default=None)
    walkie_talkie_mark = models.IntegerField(choices=CHOICES, default=None)
    walkie_talkie_comment = models.CharField(_('Comment'), max_length=40, default=None)
    reflective_vest_mark = models.IntegerField(choices=CHOICES, default=None)
    reflective_vest_comment = models.CharField(_('Comment'), max_length=40, default=None)
    scraper_brush_mark = models.IntegerField(choices=CHOICES, default=None)
    scraper_brush_comment = models.CharField(_('Comment'), max_length=40, default=None)
    # next step
    driver_license_mark = models.IntegerField(choices=CHOICES, default=None)
    driver_license_comment = models.CharField(_('Comment'), max_length=40, default=None)
    car_docs_mark = models.IntegerField(choices=CHOICES, default=None)
    car_docs_comment = models.CharField(_('Comment'), max_length=40, default=None)
    cargo_docs_mark = models.IntegerField(choices=CHOICES, default=None)
    cargo_docs_comment = models.CharField(_('Comment'), max_length=40, default=None)
    # next step
    corrective_actions = models.CharField(_('Corrective action'), max_length=100, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
      

