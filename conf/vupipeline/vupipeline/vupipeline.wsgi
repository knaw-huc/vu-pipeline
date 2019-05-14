from vupipeline import vupipeline
import clam.clamservice
application = clam.clamservice.run_wsgi(vupipeline)