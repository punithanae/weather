

import python_weather

import asyncio


async def getweather():
  place='Thirumalapadi'
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    weather = await client.get(place)

    celcius= (int(weather.current.temperature) - 32) * 0.5556
    print(f'{place} temperature is {weather.current.temperature}°C')




async def main():
    await getweather()

if __name__ == "__main__":
    asyncio.run(main())