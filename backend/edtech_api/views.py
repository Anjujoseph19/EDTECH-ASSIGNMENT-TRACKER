from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Assignment, Submission
from .serializers import AssignmentSerializer, SubmissionSerializer

@api_view(['POST'])
def create_assignment(request):
    if request.user.role != 'teacher':
        return Response({'error': 'Only teachers can create assignments'}, status=403)
    serializer = AssignmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def submit_assignment(request, id):
    if request.user.role != 'student':
        return Response({'error': 'Only students can submit assignments'}, status=403)
    try:
        assignment = Assignment.objects.get(id=id)
    except Assignment.DoesNotExist:
        return Response({'error': 'Assignment not found'}, status=404)

    serializer = SubmissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(student=request.user, assignment=assignment)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def view_submissions(request, assignment_id):
    if request.user.role != 'teacher':
        return Response({'error': 'Only teachers can view submissions'}, status=403)
    submissions = Submission.objects.filter(assignment_id=assignment_id)
    serializer = SubmissionSerializer(submissions, many=True)
    return Response(serializer.data)
