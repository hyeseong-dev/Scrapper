import asyncio
import yaml
import aiofiles
import os
import types


async def load_env(file_path: str, filename: str = "env.yaml"):
    file_abs_path = f"{file_path}/{filename}"
    if os.path.isfile(file_abs_path):
        async with aiofiles.open(file_abs_path, mode="r") as f:
            file_content = await f.read()
            config = yaml.load(file_content, Loader=yaml.FullLoader)
        config = types.SimpleNamespace(**config)
        return config

    else:
        print(file_abs_path)
        raise FileNotFoundError(f"{file_abs_path} not found")


if __name__ == "__main__":
    import os
    async def main():
        config_path = f"{os.getcwd()}/config"
        env = await load_env(config_path, "env.yaml")
        print(env.DEV)

    asyncio.run(main())
