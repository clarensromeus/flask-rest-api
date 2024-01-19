from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field , AliasChoices, StrictStr



def Configuration(ENV_FILE: str):
    
    class Settings(BaseSettings):
        # global environment model configuration
        model_config = SettingsConfigDict(env_file=ENV_FILE, env_file_encoding="utf-8", env_prefix="FLASK_", case_sensitive=True, 
                                          extra="ignore", str_strip_whitespace=True, str_to_lower=True)

        # all fields declaration                                 
        PROJECT_MODE: str = Field(default="developement", description="MODE", title="project running mode", examples=["developement", "production"])

        PROJECT_NAME: StrictStr = Field(default="Techycompagny.com", max_length=40, min_length=5, description="PROJECT_NAME",
                                        title="on-the-fly project name", validate_default=True, examples=["Facebook.com", "Google.com"])
        PROJECT_VERSION: StrictStr = Field(default="0.0.1", description="PROJECT_VERSION", title="last released project version", validate_default=True)
        PROJECT_OWNER: StrictStr = Field(default="MarkZukerberg", min_length=5, max_length=40, description="PROJECT_OWNER",
                                         title="project owner name", validate_default=True)

        PROJECT_DEBUG: bool = Field(default=False, description="PROJECT_DEBUG", title="project debugging mode", validate_default=True)
        DATABASE_USERNAME: str = Field(default="GautamAdami", min_length=3, max_length=40, description="DATABASE_USERNAME", 
                                             title="project database username", validate_default=True, examples=["Billgates","Steevejobs"])
        DATABASE_PASSWORD: StrictStr = Field(default="Romeus(+-2999)", max_length=50, min_length=2, description="DATABASE_PASSWORD",
                                             title="project secure database password", validate_default=True)

        DATABASE_HOST: int | str = Field(default="localhost", description="DATABASE_HOST", title="project database host", validate_default=True)
        DATABASE_PORT: int = Field(default=3306, description="DATABASE_PORT", title="project database port", validate_default=True)
        DATABASE_NAME: StrictStr = Field(default="Techycohort", min_length=5, max_length=50, description="DATABASE_NAME", 
                                         title="project database name", examples=["TECHY", "SCHOOLBOARD"])

        SQLALQUEMY_DATABASE_URI: str = Field(default="database+driver://username:password@127.0.0.1:3306/database_name", description="SQLALQUEMY_DATABASE_URI",
                                             title="FULL SQLALQUEMY DATABASE URI", validate_default=True)
        DATABASE_TRACK_MODIFICATION: bool = Field(default=False, alias_priority=2, validation_alias=AliasChoices("FLASK_SQLALQUEMY_TRACK_MODIFICATION", "TRACK_MODIFICATION"), 
                                                  description="DATABASE_TRACK_MODIFICATION", title="database tracking modification", validate_default=True)

    # after automatic validation of the setting model class by pydantic now
    # i on my own do the model serialization
    return Settings().model_dump()