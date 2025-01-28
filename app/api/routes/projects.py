from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.project import ProjectCreate, ProjectResponse, ProjectUpdate
from app.models.project import Project
from app.auth.dependencies import get_current_user, get_admin_user
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=List[ProjectResponse])
async def get_projects(_: User = Depends(get_current_user)):
    projects = Project.objects.all()
    return [ProjectResponse(
        id=str(project.id),
        name=project.name,
        description=project.description,
        created_at=project.created_at,
        updated_at=project.updated_at
    ) for project in projects]
 
@router.post("/", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
async def create_project(
    project_data: ProjectCreate,
    _: User = Depends(get_admin_user)
):
    project = Project(**project_data.model_dump())
    project.save()
    return ProjectResponse(
        id=str(project.id),
        name=project.name,
        description=project.description,
        created_at=project.created_at,
        updated_at=project.updated_at
    )

@router.put("/{project_id}", response_model=ProjectResponse)
async def update_project(
    project_id: str,
    project_data: ProjectUpdate,
    _: User = Depends(get_admin_user)
):
    project = Project.objects(id=project_id).first()
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    update_data = {k: v for k, v in project_data.model_dump().items() if v is not None}
    Project.objects(id=project_id).update_one(**update_data)
    project.reload()
    
    return ProjectResponse(
        id=str(project.id),
        name=project.name,
        description=project.description,
        created_at=project.created_at,
        updated_at=project.updated_at
    )

@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(
    project_id: str,
    _: User = Depends(get_admin_user)
):
    project = Project.objects(id=project_id).first()
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    project.delete()
