from main import main_flow
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule


deployment = Deployment.build_from_flow(
    flow=main_flow,
    name="Traffic crashes deployment",
    version="1",
    schedule=(CronSchedule(cron="0 0 * * *", timezone="America/Chicago"))

)

if __name__ == '__main__':
    deployment.apply()
