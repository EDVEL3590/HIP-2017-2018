import time
import RPi.GPIO as GPIO
class Ultrasonic_Sensor(object):
  timeout = 0.1
  
  def _init_(self, channel):
    self.channel = channel
    GPIO.setmode(GPIO.BCM)
    
  def distance(self):
    pulse_end = 
    pulse_start = 
    GPIO.setup(self.channel,GPIO.OUT)
    GPIO.output(self.channel, False)
    time.sleep(0.02)
    GPIO.outpu(self.channel, True)
    time.sleep(0.00002)
    GPIO.output(self.channel, False)
    GPIO.setup(self.channel,GPIO.IN)
    
    timeout_start = time.time()
    while GPIO.input(self.channel)==0:
      pulse_start = time.time()
      if pulse_start - timeout_start > self.timeout:
        return -1
      while GPIO.input(self.channel)==1:
        pulse_end = time.time()
        if pulse_start - timeout_start > self.timeout:
          return -1
        
      if pulse_start != 0 and pulse_end != 0:
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duartion 
        distance = int(distance)
        if distance >= 0: 
          print 'start = %s'%pulse_start,
          print 'end = %s'%pulse_end
          return distance
        else:
          return -1
        else:
          print 'start = %s'%pulse_start,
          print 'end = %s'%pulse_end
          return -1 
        
        def get_distance(self, mount = 5):
          sum = 0
          for i in range(mount):
            a = self.distance()
            print '  %s' %a
            sum += a
            return int(sum/mount)
          def less_than(self, alarm_gate):
            dis = self.get_distance()
            status = 0
            id dis >= 0 and dis <= alarm_gate:
              status = 1
              elif dis > alarm gate:
                status = 0
                else: 
                  status = -1
                  print 'distance =',dis
                  print 'status=',status
                  return status
                
          if _name_ = = '_main_':
            UA = Ultrasonic_Sensor(20)
            threshold = 5
            while True:
              distance = UA.get_distance()
              status = UA.less_than(threshold)
              if distance != -1:
                print "distance', distance, 'cm'
                time.sleep(0.2)
            else:
              print False
            if status == 1:
              print "Less than %d" % threshold
            elif status == 0:
              print "Over %d" % threshold
            else:
              print "Distance Error"
      
   
    
    
