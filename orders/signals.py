from django.dispatch import Signal, receiver
from vendors.models import HistoricalPerformance

# Performance History model reference
performance_history_model = HistoricalPerformance

# signals for calcluating vendor performance matrix based on acknowledgement and
# completion of purchase order status
purchase_order_status_completed = Signal()
purchase_order_acknowledged = Signal()


@receiver(signal=purchase_order_status_completed)
def calc_perfomance_matrix(sender, instance, **kwargs):
    vendor = instance.vendor
    # calculate matrix
    on_time_delivery_rate = vendor.calc_on_time_delivery_rate()
    quality_rating_avg = vendor.calc_avg_quality_ratings()
    fulfillment_rate = vendor.calc_fulfillment_rate()

    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.quality_rating_avg = quality_rating_avg
    vendor.fulfillment_rate = fulfillment_rate
    vendor.save()
    vendor.refresh_from_db()

    # create performance history
    performance_history_model.objects.create(
        vendor=vendor,
        on_time_delivery_rate=on_time_delivery_rate,
        quality_rating_avg=quality_rating_avg,
        fulfillment_rate=fulfillment_rate,
        average_response_time=vendor.average_response_time,
    )
    return vendor


@receiver(signal=purchase_order_acknowledged)
def calc_avg_response_time(sender, instance, **kwargs):
    vendor = instance.vendor
    vendor.avg_response_time = vendor.calc_avg_response_time()
    vendor.save()
    return vendor
