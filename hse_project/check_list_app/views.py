from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CheckList
from .forms import CheckListForm
from django.contrib import messages
from django.utils.translation import gettext as _

def index(request):
    return render(request, 'index.html')

@login_required
def select(request):
    return render(request, 'select.html')

@login_required
def regular(request):
    if request.method == 'POST':
        form = CheckListForm(request.POST)
        if form.is_valid():
            # print(form)
            cd = form.cleaned_data
            # print(cd)
            check_list = CheckList(date=cd['date'],
                                   car=cd['car'],
                                   driver=cd['driver'],
                                   fuel_mark=cd['fuel_mark'],
                                   fuel_comment=cd['fuel_comment'],
                                   oil_mark=cd['oil_mark'],
                                   oil_comment=cd['oil_comment'],
                                   brake_fluid_mark=cd['brake_fluid_mark'],
                                   brake_fluid_comment=cd['brake_fluid_comment'],
                                   cooling_fluid_mark=cd['cooling_fluid_mark'],
                                   cooling_fluid_comment=cd['cooling_fluid_comment'],
                                   windshield_fluid_mark=cd['windshield_fluid_mark'],
                                   windshield_fluid_comment=cd['windshield_fluid_comment'],
                                   headlights_mark=cd['headlights_mark'],
                                    headlights_comment=cd['headlights_comment'],
                                    revers_lights_mark=cd['revers_lights_mark'],
                                    revers_lights_comment=cd['revers_lights_comment'],
                                    turn_stop_ind_mark=cd['turn_stop_ind_mark'],    
                                    turn_stop_ind_comment=cd['turn_stop_ind_comment'],
                                    wheel_mark=cd['wheel_mark'],
                                    wheel_comment=cd['wheel_comment'], 
                                    clutch_mark=cd['clutch_mark'],
                                    clutch_comment=cd['clutch_comment'],
                                    brake_mark=cd['brake_mark'], 
                                    brake_comment=cd['brake_comment'], 
                                    monitor_device_mark=cd['monitor_device_mark'], 
                                    monitor_comment=cd['monitor_comment'], 
                                    heater_cond_mark=cd['heater_cond_mark'], 
                                    heater_cond_comment=cd['heater_cond_comment'], 
                                    wipers_mark=cd['wipers_mark'],
                                    wipers_comment=cd['wipers_comment'], 
                                    beep_mark=cd['beep_mark'],
                                    beep_comment=cd['beep_comment'], 
                                    beep_reverse_mark=cd['beep_reverse_mark'], 
                                    beep_reverse_comment=cd['beep_reverse_comment'],
                                    gps_mark=cd['gps_mark'], 
                                    gps_comment=cd['gps_comment'], 
                                    dvr_mark=cd['dvr_mark'], 
                                    dvr_comment=cd['dvr_comment'], 
                                    battery_mark=cd['battery_mark'], 
                                    battery_comment=cd['battery_comment'],
                                    inside_out_mark=cd['inside_out_mark'], 
                                    inside_out_comment=cd['inside_out_comment'],
                                    mirrors_glass_mark=cd['mirrors_glass_mark'],
                                    mirrors_glass_comment=cd['mirrors_glass_comment'],
                                    seat_belts_mark=cd['seat_belts_mark'],
                                    seat_belts_comment=cd['seat_belts_comment'],
                                    tires_press_mark=cd['tires_press_mark'],
                                    tires_press_comment=cd['tires_press_comment'],
                                    disks_mark=cd['disks_mark'],
                                    disks_comment=cd['disks_comment'],
                                    number_mark=cd['number_mark'],
                                    number_comment=cd['number_comment'],
                                    wheel_nuts_mark=cd['wheel_nuts_mark'],
                                    wheel_nuts_comment=cd['wheel_nuts_comment'],
                                    extingusher_mark=cd['extingusher_mark'],
                                    extingusher_comment=cd['extingusher_comment'],
                                    first_aid_kit_mark=cd['first_aid_kit_mark'],
                                    first_aid_kit_comment=cd['first_aid_kit_comment'],
                                    car_tools_mark=cd['car_tools_mark'],
                                    car_tools_comment=cd['car_tools_comment'],
                                    spare_wheel_mark=cd['spare_wheel_mark'],
                                    spare_wheel_comment=cd['spare_wheel_comment'],
                                    warning_triangle_mark=cd['warning_triangle_mark'],
                                    warning_triangle_comment=cd['warning_triangle_comment'],
                                    tow_rope_mark=cd['tow_rope_mark'],
                                    tow_rope_comment=cd['tow_rope_comment'],
                                    wheel_chocks_mark=cd['wheel_chocks_mark'],
                                    wheel_chocks_comment=cd['wheel_chocks_comment'],
                                    walkie_talkie_mark=cd['walkie_talkie_mark'],
                                    walkie_talkie_comment=cd['walkie_talkie_comment'],
                                    reflective_vest_mark=cd['reflective_vest_mark'],
                                    reflective_vest_comment=cd['reflective_vest_comment'],
                                    scraper_brush_mark=cd['scraper_brush_mark'],
                                    scraper_brush_comment=cd['scraper_brush_comment'],
                                    driver_license_mark=cd['driver_license_mark'],
                                    driver_license_comment=cd['driver_license_comment'],
                                    car_docs_mark=cd['car_docs_mark'],
                                    car_docs_comment=cd['car_docs_comment'],
                                    cargo_docs_mark=cd['cargo_docs_mark'],
                                    cargo_docs_comment=cd['cargo_docs_comment'],
                                    corrective_actions=cd['corrective_actions'],  
                                    )

            # print(check_list)
            check_list.user = request.user
            check_list.save()
            messages.success(request, _('Your form has been successfully completed.'))
            return redirect('index')
    else:
        form = CheckListForm()

    return render(request, 'regular.html', context={'form': form})